# Deployment

There are 2 different remote:
- origin: Pelican conf
- pages: Github pages

## Publish to Github Pages

```shell
$ make publish
$ ghp-import output -b gh-pages
$ git push pages gh-pages:master
```

inline:
```shell
$ make publish && ghp-import output -b gh-pages && git push pages gh-pages:master
```

# How to use Pelican

## Commands frequently used
- Start dev server: `make devserver`


The command:
ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH=gh-pages) $(OUTPUTDIR=output)
