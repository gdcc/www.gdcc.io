# dataversecommunity.global

This GitHub project hosts the sources from which the GDCC website at https://dataversecommunity.global is built.
Builds are automated and any commited changes will be released by automation.

You can do smaller edits using the GitHub integrated web editor for files and change the Markdown based content.
For larger changes, we recommend working with a local setup, also allowing to preview your changes.
See below for a tutorial how to start your local setup.

## Prepare your environment

First, install Python 3.9 (or later).

Additionally, you need to [install `poetry >= 1.2.0`](https://python-poetry.org/docs/#installation), either globally, or within an environment of your choice.
As a project, we chose `poetry` to manage our dependencies, builds, and deposits as a state of the art solution within the Python ecosystem.

## Get the source code

Next, you need to obtain a version of the website "source code".

You can either download it as a zipped package or clone the whole Git repository.
You can clone the repository and enter the project directory as follows:

```shell
git clone https://github.com/gdcc/dataversecommunity.global.git
cd dataversecommunity.global
```

## Build the website for preview

To build the website in your *poetry* environment, run the
following commands from the project root:

```shell
poetry install
poetry run task docs-build
```

On Linux you can use `xdg-open`, on Mac `open` to see the built output in your browser:
```shell
xdg-open build/html/index.html
```

Or use [`sphinx-autobuild`](https://github.com/executablebooks/sphinx-autobuild) to enable a self-updating preview service:

```shell
poetry install
poetry run task docs-live
```

The page will automatically be opened for you in a browser window or tab.
**Note:** enabling auto-reload without user interaction requires you to install the "LiveReload" extension for your browser.