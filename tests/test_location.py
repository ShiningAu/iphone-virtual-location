import asyncio
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import AsyncMock

spec = importlib.util.spec_from_file_location('iphone_location', Path(__file__).resolve().parents[1] / 'src' / 'iphone_location.py')
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class LocationTests(unittest.TestCase):
    def test_negative_longitude_is_passed_as_a_coordinate(self):
        args = app.parse_args(['start', '--lat', '40.7128', '--lon', '-74.006'])
        self.assertEqual(app.build_device_command(args)[-3:], ['--', '40.7128', '-74.006'])

    def test_invalid_and_partial_coordinates_are_rejected(self):
        for arguments in (['start', '--lat', '91', '--lon', '0'], ['start', '--lat', 'nan', '--lon', '0'], ['start', '--lat', '1']):
            with self.assertRaises(SystemExit):
                app.parse_args(arguments)

    def test_clear_is_requested_when_input_is_closed(self):
        location = AsyncMock()
        def closed_input(prompt):
            raise EOFError('No terminal')
        with self.assertRaises(EOFError):
            asyncio.run(app.hold_location(location, 1, 2, closed_input))
        location.clear.assert_awaited_once()

    def test_input_wait_keeps_the_async_loop_responsive(self):
        import threading
        async def scenario():
            finished = threading.Event()
            location = AsyncMock()
            def wait(prompt):
                if not finished.wait(2):
                    raise TimeoutError('Event loop was blocked')
            task = asyncio.create_task(app.hold_location(location, 1, 2, wait))
            await asyncio.sleep(0.02)
            finished.set()
            await task
            location.clear.assert_awaited_once()
        asyncio.run(scenario())

    def test_dependency_injection_registers_a_valid_cli_command(self):
        app.configure_runtime()
        from pymobiledevice3.cli.developer.dvt.simulate_location import cli
        from typer.main import get_command
        command = get_command(cli).commands['set']
        parameters = {parameter.name for parameter in command.params}
        self.assertIn('latitude', parameters)
        self.assertIn('longitude', parameters)
        self.assertIn('udid', parameters)


if __name__ == '__main__':
    unittest.main()
