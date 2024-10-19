class SimulationMetrics:
    def __init__(self):
        # Initialize metrics with default values
        self.air_quality_improvement = 0.0  # Percentage improvement in air quality
        self.traffic_reduction = 0.0  # Percentage reduction in traffic congestion
        self.livability_score = 0.0  # A composite score based on noise, safety, pollution, etc.
        self.noise_reduction = 0.0  # Percentage reduction in noise pollution
        self.data_history = []  # A log to store metrics over time

    def calculate_air_quality_reduction(self, before, after):
        # Calculate air quality improvement based on before and after pollution levels
        if before > 0:
            self.air_quality_improvement = ((before - after) / before) * 100
        else:
            self.air_quality_improvement = 0
        self.log_metric("air_quality_improvement", self.air_quality_improvement)
        return self.air_quality_improvement

    def calculate_traffic_reduction(self, initial_traffic, current_traffic):
        # Calculate traffic reduction percentage
        if initial_traffic > 0:
            self.traffic_reduction = ((initial_traffic - current_traffic) / initial_traffic) * 100
        else:
            self.traffic_reduction = 0
        self.log_metric("traffic_reduction", self.traffic_reduction)
        return self.traffic_reduction

    def calculate_livability_score(self, noise_reduction, air_quality_improvement):
        # Calculate a composite livability score based on noise reduction and air quality improvement
        self.livability_score = (noise_reduction * 0.4) + (air_quality_improvement * 0.6)
        self.log_metric("livability_score", self.livability_score)
        return self.livability_score

    def calculate_noise_reduction(self, before_noise, after_noise):
        # Calculate noise reduction percentage
        if before_noise > 0:
            self.noise_reduction = ((before_noise - after_noise) / before_noise) * 100
        else:
            self.noise_reduction = 0
        self.log_metric("noise_reduction", self.noise_reduction)
        return self.noise_reduction

    def get_metrics(self):
        # Return the current metrics in a dictionary
        return {
            "air_quality_improvement": self.air_quality_improvement,
            "traffic_reduction": self.traffic_reduction,
            "livability_score": self.livability_score,
            "noise_reduction": self.noise_reduction
        }

    def log_metric(self, metric_name, value):
        # Log the metric into the data history
        self.data_history.append({"metric": metric_name, "value": value, "timestamp": self.get_current_time()})

    def get_current_time(self):
        # Simulate getting the current time for logging
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S")

    def get_data_history(self):
        # Return the log of all recorded metrics
        return self.data_history

# Example Usage:
metrics = SimulationMetrics()

# Simulate calculating metrics during the simulation
initial_pollution = 100  # Air quality index before
current_pollution = 80   # Air quality index after
initial_traffic = 1000   # Initial number of vehicles
current_traffic = 800    # Current number of vehicles
initial_noise = 70       # Noise level before
current_noise = 50       # Noise level after

# Calculate metrics
air_quality = metrics.calculate_air_quality_reduction(initial_pollution, current_pollution)
traffic_reduction = metrics.calculate_traffic_reduction(initial_traffic, current_traffic)
noise_reduction = metrics.calculate_noise_reduction(initial_noise, current_noise)

# Calculate overall livability score
livability = metrics.calculate_livability_score(noise_reduction, air_quality)

# Get current metrics
print(metrics.get_metrics())

# Get data history
print(metrics.get_data_history())
