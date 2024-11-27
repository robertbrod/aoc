#### Advent of Code Automation

This repo follows the automation guidelines on the r/adventofcode community [wiki](https://www.reddit.com/r/adventofcode/wiki/faqs/automation)

- Outbound calls are throttled to every 10 minutes in `aoc_gateway.fetch_input`
- Once inputs are downloaded, they are cached locally (`util.cache_input_data`)
  - If you suspect your input is corrupted, you can manually request a fresh copy by deleting cached copy on disk and restarting script
- The `User-Agent` header in `aoc_gateway.fetch_input` is set to me since I maintain this tool! :)
