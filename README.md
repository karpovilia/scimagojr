## scimaojr

Tiny script for downloading scimaojr journals rating. The main project downloads journals and their meta, given the list of science areas. 
All industries along with their codes can be found in [areas.json](https://github.com/karpovilia/scimagojr/blob/master/areas.json) file.

Data for March 31, 2020 can be found [here](https://dl.dropbox.com/s/06ni77wvrhukth3/scimagojr_full_2020-03-31.csv)

vscode `launch.json` example:
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "./scimagojr/src/__main__.py",
            "console": "integratedTerminal"
        }
    ]
}
```

Example of resuling csv filtering can be found at [analysis.ipynb](https://github.com/karpovilia/scimagojr/blob/master/analysis.ipynb)
