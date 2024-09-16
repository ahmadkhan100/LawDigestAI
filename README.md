
# LawDigestAI

![Build Status](https://github.com/ahmadkhan100/LawDigestAI/actions/workflows/python-app.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

LawDigestAI is an open-source AI platform that leverages advanced machine learning techniques to automatically summarize unstructured legal documents. It aims to assist legal professionals in quickly understanding the core elements of lengthy documents, enhancing efficiency and decision-making.

## Features

- **Supports Various Legal Documents**: Handles contracts, court judgments, patents, and more.
- **Accurate Summarization**: Generates concise and precise summaries tailored to legal contexts.
- **Easy Integration**: Seamlessly integrates with existing systems via API.
- **Extensible**: Easily extendable to incorporate additional features like keyword extraction and entity recognition.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Summarizing a Document](#summarizing-a-document)
  - [API Integration](#api-integration)
- [Contributing](#contributing)
- [License](#license)
- [Code of Conduct](#code-of-conduct)

## Installation

Refer to the [Installation Guide](docs/installation.md) for detailed setup instructions.

### Prerequisites

- **Python**: Version 3.8 or higher
- **pip**: Python package installer

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ahmadkhan100/LawDigestAI.git
   cd LawDigestAI
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Data**

   Place your raw legal documents in the `data/raw/` directory and run the preprocessing script:

   ```bash
   python src/data_preprocessing.py
   ```

5. **Run the Summarizer**

   ```bash
   python src/summarization.py
   ```

## Usage

Refer to the [Usage Guide](docs/usage.md) for detailed instructions on how to use LawDigestAI.

### Summarizing a Document

You can use the `LawDigestAI` class to summarize legal documents.

#### Example

```python
from src.summarization import LawDigestAI

summarizer = LawDigestAI()
text = "Your legal document text here."
summary = summarizer.summarize(text)
print(summary)
```

### API Integration

To integrate the summarizer into a web application, consider using Flask.

#### Example Flask App

```python
from flask import Flask, request, jsonify
from src.summarization import LawDigestAI

app = Flask(__name__)
summarizer = LawDigestAI()

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided.'}), 400
    summary = summarizer.summarize(text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
```

### Running the Flask App

1. Ensure all dependencies are installed.
2. Run the Flask application:

   ```bash
   python path_to_flask_app.py
   ```

3. Send a POST request to `http://localhost:5000/summarize` with JSON payload:

   ```json
   {
     "text": "Your legal document text here."
   }
   ```

## Contributing

We welcome contributions! Please read our [Contribution Guidelines](docs/contribution.md) to get started.

### How to Contribute

1. **Fork the Repository**

   Click the "Fork" button at the top right of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/ahmadkhan100/LawDigestAI.git
   cd LawDigestAI
   ```

3. **Create a New Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**

5. **Commit Your Changes**

   ```bash
   git commit -m "Add your message here"
   ```

6. **Push to Your Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**

   Go to the original repository and click "New Pull Request."

### Code of Conduct

Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

### Reporting Issues

Use the [Issues](https://github.com/ahmadkhan100/LawDigestAI/issues) section to report bugs or suggest features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to understand the standards for participation in this project.

---

## Getting Started

To get started with LawDigestAI, follow the installation steps above and refer to the documentation for detailed usage instructions. Whether you're a legal professional looking to streamline document analysis or a developer aiming to contribute to the project, LawDigestAI offers the tools and flexibility you need.

For any questions or support, feel free to open an issue in the [Issues](https://github.com/yourusername/LawDigestAI/issues) section of the repository.

---

**Happy Summarizing!**
   

