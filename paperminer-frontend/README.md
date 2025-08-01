# PaperMiner Frontend

A modern React frontend for the PaperMiner application that searches PubMed for papers with non-academic authors from pharmaceutical/biotech companies.

## Features

- 🎨 Modern, responsive UI with Tailwind CSS
- 🔍 Real-time PubMed search
- 📊 Interactive results table
- 📥 CSV download functionality
- ⚡ Fast development with Vite
- 🎯 TypeScript for type safety

## Tech Stack

- **React 18** with TypeScript
- **Vite** for fast development and building
- **Tailwind CSS 3.4** for styling
- **FastAPI** backend integration

## Getting Started

### Prerequisites

- Node.js 18+ 
- Python 3.8+ (for backend)

### Installation

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Open [http://localhost:5173](http://localhost:5173) in your browser.

### Backend Setup

1. Navigate to the Python backend directory:
```bash
cd ../Python
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Start the FastAPI backend:
```bash
python backend.py
```

The backend will be available at [http://localhost:8000](http://localhost:8000).

## Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

### Project Structure

```
src/
├── components/          # React components
│   ├── SearchForm.tsx  # Search form component
│   ├── ResultsTable.tsx # Results display table
│   └── ErrorDisplay.tsx # Error handling component
├── api.ts              # API service layer
├── types.ts            # TypeScript type definitions
├── App.tsx             # Main application component
└── index.css           # Tailwind CSS styles
```

## API Endpoints

The frontend communicates with the following backend endpoints:

- `POST /api/search` - Search for papers
- `POST /api/download` - Download results as CSV
- `GET /api/health` - Health check

## Features

### Search Form
- PubMed query input with validation
- Debug mode toggle
- Loading states and error handling

### Results Table
- Sortable columns
- PubMed ID links to original papers
- Truncated text with tooltips
- Responsive design

### Error Handling
- User-friendly error messages
- Retry functionality
- Network error recovery

## Styling

The application uses Tailwind CSS for styling with:
- Responsive design
- Dark/light mode support
- Custom color scheme
- Smooth animations and transitions

## Deployment

### Build for Production

```bash
npm run build
```

The built files will be in the `dist/` directory.

### Environment Variables

Create a `.env` file for environment-specific configuration:

```env
VITE_API_BASE_URL=http://localhost:8000
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

This project is licensed under the MIT License.
