# GoPersonal Python SDK

An asynchronous Python SDK for interacting with the GoPersonal API.

## Features

- Asynchronous API calls using `aiohttp`
- Easy initialization with client credentials
- Bulk search functionality
- Supports both environment variables and direct configuration

## Installation

You can install the GoPersonal SDK using pip:

```bash
pip install gopersonal-sdk
```

## Quick Start

Here's a simple example to get you started with the GoPersonal SDK:

```python
import asyncio
import os
from gopersonal import GoPersonal

async def main():
    # Initialize the SDK
    gp = GoPersonal()
    
    try:
        # Initialize with credentials (using environment variables in this example)
        init_response = await gp.init({
            'client_id': os.environ.get('GO_PERSONAL_CLIENT_ID'),
            'client_secret': os.environ.get('GO_PERSONAL_CLIENT_SECRET')
        })
        print(f"Initialization successful. Token: {init_response['token']}")

        # Perform a bulk search
        search_results = await gp.bulk_search(["juegos", "televisor"])
        print(f"Search results: {search_results}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
```

Make sure to set your GoPersonal API credentials as environment variables:

```bash
export GO_PERSONAL_CLIENT_ID='your_client_id'
export GO_PERSONAL_CLIENT_SECRET='your_client_secret'
```

## API Reference

### `GoPersonal`

The main class for interacting with the GoPersonal API.

#### `init(config: Optional[Dict[str, str]] = None) -> Dict[str, str]`

Initializes the SDK with the provided configuration.

- `config`: A dictionary containing `client_id`, `client_secret`, and optionally `region`.
- Returns: A dictionary containing the initialization token.

#### `bulk_search(terms: List[str]) -> Dict`

Performs a bulk search using the provided terms.

- `terms`: A list of search terms.
- Returns: A dictionary containing the search results.

## Development

To set up the project for development:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gopersonal-sdk.git
   cd gopersonal-sdk
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the package in editable mode with development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

4. Run tests:
   ```bash
   pytest
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.