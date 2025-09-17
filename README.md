# LSP-zuban

This is a helper package that automatically installs and updates [zuban](https://github.com/zubanls/zuban) for you. Zuban is a high-performance Python Language Server and type checker implemented in Rust, by the author of Jedi. Zuban is 20–200× faster than Mypy, while using roughly half the memory and CPU compared to Ty and Pyrefly. It offers both a PyRight-like mode and a Mypy-compatible mode, which behaves just like Mypy; supporting the same config files, command-line flags, and error messages.

## Requirements

To use this package, you must have:

- An executable `python` (on Windows) or `python3` (on Linux/macOS)
- The [LSP](https://packagecontrol.io/packages/LSP) package
- For Ubuntu and Debian users, you must also install python3-venv with apt
- It's recommended to also install the [LSP-json](https://packagecontrol.io/packages/LSP-json) package which will provide auto-completion and validation for this package's settings.

## Configuration

There are multiple ways to configure the package and the language server.

- Global configuration: `Preferences > Package Settings > LSP > Servers > LSP-zuban`
- Project-specific configuration:
  From the Command Palette run `Project: Edit Project` and add your settings in:

```js
{
	"settings": {
		"LSP": {
			"LSP-zuban": {
				"initializationOptions": {
					"settings": {
						// Put your settings here
					}
				}
			}
		}
	}
}
```