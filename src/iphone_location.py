"""Small Windows launcher for pymobiledevice3's DVT location service."""

import argparse
import asyncio
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def coordinate(value, minimum, maximum):
    number = float(value)
    if not math.isfinite(number) or not minimum <= number <= maximum:
        raise argparse.ArgumentTypeError(f'Coordinate must be between {minimum} and {maximum}.')
    return number


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='iPhone virtual location over USB (Windows).')
    sub = parser.add_subparsers(dest='command', required=True)
    start = sub.add_parser('start', help='Set and maintain a virtual location until Enter.')
    start.add_argument('--preset', default='new-york', help='Name in config/locations.json.')
    start.add_argument('--lat', type=lambda v: coordinate(v, -90, 90))
    start.add_argument('--lon', type=lambda v: coordinate(v, -180, 180))
    start.add_argument('--udid', help='Explicit target when several devices are connected.')
    clear = sub.add_parser('restore', help='Send a clear request; verify the real location in Maps.')
    clear.add_argument('--udid')
    sub.add_parser('devices', help='List locally connected USB devices; output can include identifiers.')
    args = parser.parse_args(argv)
    if args.command == 'start' and ((args.lat is None) != (args.lon is None)):
        parser.error('--lat and --lon must be supplied together.')
    return args


def build_device_command(args):
    if args.command == 'devices':
        return ['usbmux', 'list', '--usb']
    command = ['developer', 'dvt', 'simulate-location']
    command += ['set' if args.command == 'start' else 'clear']
    if args.udid:
        command += ['--udid', args.udid]
    if args.command == 'start':
        if args.lat is None:
            presets = json.loads((ROOT / 'config' / 'locations.json').read_text(encoding='utf-8'))
            if args.preset not in presets:
                raise ValueError(f'Unknown preset: {args.preset}. Available: {", ".join(presets)}')
            selected = presets[args.preset]
            lat = coordinate(selected['latitude'], -90, 90)
            lon = coordinate(selected['longitude'], -180, 180)
        else:
            lat, lon = args.lat, args.lon
        command += ['--', str(lat), str(lon)]
    return command


async def hold_location(location, latitude, longitude, wait_for_enter=input):
    try:
        await location.set(latitude, longitude)
        print(f'Sent coordinates: {latitude}, {longitude}. Confirm the blue dot in Apple Maps.')
        # A blocking input() on the event-loop thread can stall the userspace tunnel.
        await asyncio.to_thread(wait_for_enter, 'Keep USB connected. Press ENTER to stop and request restore: ')
    finally:
        await location.clear()
        print('Clear request sent. Verify the real position in Maps; restart iPhone if it remains simulated.')


def configure_runtime():
    import pymobiledevice3.common
    from pymobiledevice3.cli.cli_common import ServiceProviderDep, async_command
    from pymobiledevice3.cli.developer.dvt import simulate_location
    from pymobiledevice3.services.dvt.instruments.dvt_provider import DvtProvider
    from pymobiledevice3.services.dvt.instruments.location_simulation import LocationSimulation

    # Local state may contain pairing records. Never upload this directory.
    pymobiledevice3.common._HOMEFOLDER = ROOT / '.state'

    @async_command
    async def start_location(service_provider: ServiceProviderDep, latitude: float, longitude: float) -> None:
        async with DvtProvider(service_provider) as dvt, LocationSimulation(dvt) as location:
            await hold_location(location, latitude, longitude)

    # Register our async wait without editing installed third-party source files.
    matches = [c for c in simulate_location.cli.registered_commands if c.name == 'set']
    if len(matches) != 1:
        raise RuntimeError('Unexpected pymobiledevice3 CLI layout. Use the pinned dependency version.')
    simulate_location.cli.registered_commands.remove(matches[0])
    simulate_location.cli.command('set')(start_location)


def main(argv=None):
    args = parse_args(argv)
    try:
        command = build_device_command(args)
    except (ValueError, KeyError) as error:
        print(error, file=sys.stderr)
        return 2
    configure_runtime()
    sys.argv = [sys.argv[0], *command]
    from pymobiledevice3.__main__ import main as device_main
    return device_main()


if __name__ == '__main__':
    raise SystemExit(main())
