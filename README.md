# 256 Challenge

happy programmer's day. compress [challenge.b64](challenge.b64) as small as you can.

this is a [Hutter Prize](http://prize.hutter1.net/) style contest, but not for general compression.

- ai is allowed, but dumping the file into a model is expensive. finding the structure is what pays.
- any language. You ship a repo with a `Dockerfile` that builds and runs your answer.

## Score

```
score = size(compressed output) + size(your repo except Dockerfile and .git)
```

lower is better. Libraries, payloads, extra files all count.

```
docker run --network none IMAGE --compress   /data/in  /data/out
docker run --network none IMAGE --decompress /data/out /data/back
```

`/data/back` must match the original file byte for byte.

**build and run have no network.** nothing is downloaded.
`FROM` only works if that image is already on the machine.
the public runner has `python:3.12-alpine`, `alpine:3.21`, `gcc:14-bookworm`, `golang:1.23-alpine`, and `rust:1.83-alpine`. Anything else: `FROM scratch` and ship the files (they count).

`--compress` and `--decompress` have 60 seconds each. The build has 5 minutes. Clone has 2 minutes. Over that, a mismatch, or a network call at build/run is a fail.

## Submit

1. put a `Dockerfile` in your own public repo (root, or set `dir`).
2. fork this repo, add yourself to [participants.json](participants.json), open a PR.

```json
{
  "name": "your-github-username",
  "repository": "https://github.com/you/your-256-repo"
}
```

optional: `"branch": "main"`, `"dir": "subdir"`.

[256-example-solution](https://github.com/birlug/256-example) embeds the file and writes an empty compressed output. valid, terrible score.

## Scoreboard

[SCOREBOARD.md](SCOREBOARD.md)

---

### For agents

```
# your solution repo:
#   Dockerfile + program
#   entrypoint: --compress /data/in /data/out
#               --decompress /data/out /data/back
# local check:
python3 score.py challenge.b64 /path/to/your/repo

# then PR this repo:
git clone <this-repo>
# add an object to participants.json:
#   {"name":"<github-username>","repository":"https://github.com/<you>/<repo>"}
git checkout -b add-<github-username>
git add participants.json
git commit -m "add <github-username>"
git push -u origin add-<github-username>
# open a pull request
```
