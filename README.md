# Deployment
2 different remote:
- origin: Pelican conf
- pages: Github pages

## Command to publish in Github Pages

```shell
$ make publish
$ ghp-import output -b gh-pages
$ git push pages gh-pages:master
```

inline:
```shell
$ make publish && ghp-import output -b gh-pages && git push pages gh-pages:master
```