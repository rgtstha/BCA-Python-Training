# Abstraction

- Abstraction is the process of hiding the internal details and showing only the functionality.

- Abstraction can be achieved with either abstract classes or interfaces (which you will learn more about in the next chapter).

- Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasses.

- Abstract classes are denoted by the @abstractmethod decorator.

- Abstract methods are methods that are declared, but contains no implementation.


In Python, we can create abstract classes by inheriting from the ABC class of the abc module.

```python   
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} started")

    def stop(self):
        print(f"{self.name} stopped")

car = Car("Honda City")
car.start()
car.stop()
```


simple example of a network request and caching using an abstract class in Python. We'll define an abstract class representing a data fetcher, and then create concrete subclasses for fetching data from the network and implementing a basic caching mechanism.

```python
from abc import ABC, abstractmethod

class DataFetcher(ABC):
    @abstractmethod
    def fetch_data(self, key):
        pass

class NetworkDataFetcher(DataFetcher):
    def fetch_data(self, key):
        # Simulate fetching data from a network
        print(f"Fetching data from network for key: {key}")
        # In a real-world scenario, you would make an actual network request here
        return f"Network data for {key}"

class CachingDataFetcher(DataFetcher):
    def __init__(self, data_fetcher):
        self.data_fetcher = data_fetcher
        self.cache = {}

    def fetch_data(self, key):
        # Check if data is present in the cache
        if key in self.cache:
            print(f"Fetching data from cache for key: {key}")
            return self.cache[key]
        else:
            # If not present in the cache, fetch data from the underlying data fetcher
            data = self.data_fetcher.fetch_data(key)
            # Store the data in the cache for future use
            self.cache[key] = data
            return data

# Example usage:
    # Create a network data fetcher
network_fetcher = NetworkDataFetcher()

# Create a caching data fetcher using the network fetcher
caching_fetcher = CachingDataFetcher(network_fetcher)

# Fetch data using the caching fetcher
result1 = caching_fetcher.fetch_data("key1")
result2 = caching_fetcher.fetch_data("key2")
result3 = caching_fetcher.fetch_data("key1")  # This should be fetched from the cache

print(result1)
print(result2)
print(result3)

```