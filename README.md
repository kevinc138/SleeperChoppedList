# Sleeper League Analyzer

A Python tool to analyze Sleeper fantasy football leagues with a focus on guillotine league risk assessment. Outputs color-coded Excel files and CSV data for strategic decision making.

## Features

- **Real-time Risk Assessment**: Teams sorted by lowest projected points first (most at risk)
- **Live Game Tracking**: Shows how many starters have played vs total starters
- **Active Team Filtering**: Automatically excludes eliminated teams (0 projections)
- **Dual Output Formats**: 
  - CSV for data analysis
  - **Styled Excel with color-coded risk levels**
- **Weekly Projections**: Uses Sleeper's official projection API
- **Guillotine League Optimized**: Perfect for tracking elimination risk

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

The tool generates two files:
- **CSV file**: `sleeper_league_{league_id}_week_{week}.csv` - Raw data for analysis
- **Excel file**: `sleeper_league_{league_id}_week_{week}.xlsx` - **Color-coded risk visualization**

### Excel Color Coding

- 🔴 **Light Red**: Top 2 teams (highest elimination risk)
- 🟡 **Light Yellow**: Next 3 teams (medium risk)  
- 🟢 **Light Green**: Remaining teams (lower risk)
- 🔘 **Gray Headers**: Bold formatting for easy reading

### Output Columns

- **Risk Rank**: Team ranking by elimination risk (1 = most at risk)
- **Team Name**: Owner display name
- **Current Points**: Live scoring from games in progress
- **Projected Points**: Weekly projected points total
- **Starters Played**: Number of starters whose games have started
- **Total Starters**: Total number of starting positions filled

## Perfect for Guillotine Leagues

- **Risk-based rankings**: Lowest projected points first
- **Active teams only**: Eliminated teams automatically filtered out
- **Visual risk assessment**: Instant color-coded danger zones
- **Live tracking**: Monitor starter status throughout game day

## Technical Details

- Uses Sleeper's official projection API with proper parameters
- Real-time starter tracking based on live scoring
- Automatic column width adjustment in Excel
- Professional formatting with visual hierarchy