# Releasing ipyvizzu

ipyvizzu is distributed on [pypi](https://pypi.org/project/ipyvizzu/).

## Prerequisites

We assume that the `vizzuhq/ipyvizzu.git` remote is already added to your repository as `upstream`:

```sh
git remote add upstream git@github.com:vizzuhq/ipyvizzu.git
```

## Increase version number

If your changes are ready to release, you should increase the version number in
`setup.py`. In our example the new version will be 0.9.8. The version bump
should be in a separated commit:

```sh
git commit -m 'setup.py: version 0.9.8' setup.py
```

Tag this commit and push the tag to `upstream`:

```sh
git tag 0.9.8
git push --tags upstream main
```

In the above exmaple the `vizzuhq/ipyvizzu.git` remote was named to `upstream`.

## Create release notes

New release can be created on [github](https://github.com/vizzuhq/ipyvizzu/releases/new).
Where you can create release notes from [CHANGELOG](https://github.com/vizzuhq/ipyvizzu/blob/main/CHANGELOG.md).

 **Note:** Publishing a new release will automatically trigger the [Release ipyvizzu](https://github.com/vizzuhq/ipyvizzu/blob/main/.github/workflows/release.yml) workflow which builds and uploads the ipyvizzu package to [pypi](https://pypi.org/project/ipyvizzu/).
