# Sleeper League Analyzer

A Python tool to analyze Sleeper fantasy football leagues and output team rankings by projected points.

## Features

- Fetches league data from Sleeper API
- Sorts teams by projected points (descending)
- Tracks starter status (games played vs total starters)
- Outputs results as CSV spreadsheet
- Console display with formatted rankings

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```bash
python sleeper_league_analyzer.py <league_id>
```

### Finding Your League ID

1. Go to your Sleeper league in a web browser
2. The league ID is in the URL: `https://sleeper.app/leagues/LEAGUE_ID/team`
3. Copy the numeric league ID

### Example

```bash
python sleeper_league_analyzer.py 123456789
```

## Output

The tool generates:
- CSV file: `sleeper_league_{league_id}_week_{week}.csv`
- Console output with team rankings

### CSV Columns

- **Rank**: Team ranking by projected points
- **Team Name**: Owner display name or team identifier
- **Projected Points**: Total projected points for current week
- **Starters Played**: Number of starters whose games have started
- **Total Starters**: Total number of starting positions filled

## Notes

- The "Starters Played" feature is currently a placeholder and needs enhancement to check actual NFL game times
- Projected points come from Sleeper's current week matchup data
- Results are sorted in descending order by projected points

## Future Enhancements

- Real-time game status checking
- Historical week analysis
- Additional team statistics
- Custom formatting options