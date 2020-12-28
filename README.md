# doclick

doclick is a Python library working as a programmable pseudo-language simulating desktop actions such as clicking, sending keys etc.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install doclick.

```bash
pip install doclick
```

## Usage

```python
import doclick.doclick_core as dc

dc.execute_script("script.txt")
```
script.txt contains:
```
Click(100,100)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
