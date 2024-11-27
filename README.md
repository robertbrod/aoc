####

This repo follows the automation guidelines on the r/adventofcode community [wiki](https://www.reddit.com/r/adventofcode/wiki/faqs/automation)

- Outbound calls are throttled to every x minutes in `aoc_gateway.fetch_input`
- Once inputs are downloaded, they are cached locally (`function name`)
  - If you suspect your input is corrupted, you can manually request a fresh copy using `function name`
- The `User-Agent` header in `function name` is set to me since I maintain this tool! :)
