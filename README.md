

## Example Usage:
### YAML config: 
```bash 
autox -background --config my-config.yml
```
### JSON config: 
```bash 
autox --config my-config.json
```
### AutoX file: 
```sh
autox --config .autox --docker redis postgres
```

```sh
python -m autox --docker redis postgres --config my-config.yml
```

```sh
docker-compose build
docker-compose up
docker-compose down
```