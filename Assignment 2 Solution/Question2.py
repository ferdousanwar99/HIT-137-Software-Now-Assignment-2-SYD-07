import csv
import glob
from collections import defaultdict

def season_months():
    return {
        'Summer': [11, 0, 1],  # Dec, Jan, Feb
        'Autumn': [2, 3, 4],   # Mar, Apr, May
        'Winter': [5, 6, 7],   # Jun, Jul, Aug
        'Spring': [8, 9, 10]   # Sep, Oct, Nov
    }

def read_all_data(folder='temperatures'):
    files = glob.glob(f'{folder}/*.csv')
    if not files:
        raise FileNotFoundError(f"No CSV files found in {folder}.")
    
    data = defaultdict(lambda: defaultdict(list))
    for file in files:
        try:
            with open(file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    station = row['STATION_NAME']
                    temps = []
                    for month in reader.fieldnames[4:]:
                        try:
                            temps.append(float(row[month]))
                        except ValueError:
                            print(f"Invalid data in {file} for {station}, {month}.")
                            temps.append(None)
                    year = file.split('_')[-1][:4]  # Extract year from filename
                    data[station][year] = temps
        except Exception as e:
            print(f"Error reading {file}: {str(e)}")
    return data

def average_seasonal_temps(data):
    season_map = season_months()
    season_totals = defaultdict(list)
    for station, years in data.items():
        for year, temps in years.items():
            for season, months in season_map.items():
                valid_temps = [temps[m] for m in months if temps[m] is not None]
                if len(valid_temps) == 3:
                    avg = sum(valid_temps) / 3
                    season_totals[season].append(avg)
    averages = {season: sum(vals)/len(vals) if vals else 0 for season, vals in season_totals.items()}
    try:
        with open("average_temp.txt", "w") as f:
            for season, avg in averages.items():
                f.write(f"{season}: {avg:.2f}\n")
    except IOError:
        print("Error writing average_temp.txt.")
    return averages

def station_temp_ranges(data):
    ranges = {}
    for station, years in data.items():
        all_temps = []
        for year, temps in years.items():
            valid_temps = [t for t in temps if t is not None]
            if valid_temps:
                all_temps.extend(valid_temps)
        if all_temps:
            ranges[station] = max(all_temps) - min(all_temps)
    max_range = max(ranges.values(), default=0)
    largest = [station for station, rng in ranges.items() if rng == max_range]
    try:
        with open("largest_temp_range_station.txt", "w") as f:
            f.write("\n".join(largest))
    except IOError:
        print("Error writing largest_temp_range_station.txt.")
    return largest

def warmest_coolest_stations(data):
    means = {}
    for station, years in data.items():
        all_temps = []
        for year, temps in years.items():
            valid_temps = [t for t in temps if t is not None]
            if valid_temps:
                all_temps.extend(valid_temps)
        if all_temps:
            means[station] = sum(all_temps) / len(all_temps)
    max_mean = max(means.values(), default=0)
    min_mean = min(means.values(), default=0)
    warmest = [station for station, mean in means.items() if mean == max_mean]
    coolest = [station for station, mean in means.items() if mean == min_mean]
    try:
        with open("warmest_and_coolest_station.txt", "w") as f:
            f.write("Warmest:\n" + "\n".join(warmest) + "\nCoolest:\n" + "\n".join(coolest))
    except IOError:
        print("Error writing warmest_and_coolest_station.txt.")
    return warmest, coolest

# Usage
try:
    data = read_all_data()
    average_seasonal_temps(data)
    station_temp_ranges(data)
    warmest_coolest_stations(data)
except Exception as e:
    print(f"Error: {str(e)}")
