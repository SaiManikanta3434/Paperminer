# 🔬 PaperMiner

A modern web application for discovering papers with non-academic authors from pharmaceutical and biotech companies using PubMed data.

## ✨ Features

- **🔍 Real-time PubMed Search** - Search for papers with advanced filtering
- **📊 Interactive Results Table** - View and sort paper results with company affiliations
- **📥 CSV Export** - Download results as CSV files
- **🎨 Modern UI** - Beautiful, responsive interface with Tailwind CSS
- **⚡ Fast Performance** - Built with React, Vite, and FastAPI
- **🔧 Debug Mode** - Enable detailed logging for troubleshooting

## 🏗️ Architecture

### Frontend
- **React 18** with TypeScript
- **Vite** for fast development and building
- **Tailwind CSS 3.4** for styling
- **Modern Components** with proper error handling

### Backend
- **FastAPI** for high-performance API
- **PubMed API Integration** for paper data
- **Smart Filtering** for non-academic authors
- **CORS Support** for frontend communication

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.8+
- pip (Python package manager)

### 1. Install Dependencies

**Backend:**
```bash
cd Python
pip install -r requirements.txt
```

**Frontend:**
```bash
cd paperminer-frontend
npm install
```

### 2. Start the Application

**Option 1: Use the startup script**
```bash
python start_app.py
```

**Option 2: Start manually**

Backend (Terminal 1):
```bash
python run_backend.py
```

Frontend (Terminal 2):
```bash
cd paperminer-frontend
npm run dev
```

### 3. Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 📖 Usage

1. **Enter a PubMed Query** - Use standard PubMed search syntax
   - Example: `"cancer immunotherapy" AND "2023"[Date - Publication]`
   - Example: `"CRISPR" AND "gene editing"`

2. **Enable Debug Mode** (Optional) - For detailed logging

3. **View Results** - Papers with non-academic authors from pharmaceutical/biotech companies

4. **Download CSV** - Export results for further analysis

## 🔧 API Endpoints

### Search Papers
```http
POST /api/search
Content-Type: application/json

{
  "query": "cancer immunotherapy",
  "debug": false
}
```

### Download CSV
```http
POST /api/download
Content-Type: application/json

{
  "query": "cancer immunotherapy"
}
```

### Health Check
```http
GET /api/health
```

## 🎨 UI Components

### SearchForm
- PubMed query input with validation
- Debug mode toggle
- Loading states and error handling
- Beautiful Tailwind CSS styling

### ResultsTable
- Sortable columns
- PubMed ID links to original papers
- Truncated text with tooltips
- Responsive design
- CSV download functionality

### ErrorDisplay
- User-friendly error messages
- Retry functionality
- Network error recovery

## 🛠️ Development

### Project Structure
```
├── Python/                    # Backend
│   ├── backend.py            # FastAPI server
│   ├── cli.py               # Original CLI tool
│   ├── get_papers/          # Core PubMed logic
│   └── requirements.txt     # Python dependencies
├── paperminer-frontend/      # Frontend
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── api.ts          # API service
│   │   ├── types.ts        # TypeScript types
│   │   └── App.tsx         # Main app component
│   └── package.json        # Node dependencies
├── run_backend.py           # Backend startup script
└── start_app.py            # Complete startup script
```

### Available Scripts

**Frontend:**
```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run preview  # Preview production build
npm run lint     # Run ESLint
```

**Backend:**
```bash
python run_backend.py    # Start FastAPI server
python start_app.py      # Start with frontend instructions
```

## 🔍 How It Works

1. **Search Phase**: User enters PubMed query
2. **API Call**: Frontend sends request to FastAPI backend
3. **PubMed Search**: Backend searches PubMed using the query
4. **Paper Fetching**: Backend fetches detailed paper information
5. **Filtering**: Backend filters for non-academic authors from companies
6. **Results**: Frontend displays filtered results in a table
7. **Export**: Users can download results as CSV

## 🎯 Filtering Logic

The application identifies:
- **Non-academic authors** from pharmaceutical/biotech companies
- **Company affiliations** like "Genentech, Inc.", "Pfizer Pharmaceuticals"
- **Academic institutions** are filtered out (universities, hospitals, etc.)

## 🚀 Deployment

### Frontend Deployment
```bash
cd paperminer-frontend
npm run build
# Deploy dist/ folder to your hosting service
```

### Backend Deployment
```bash
# Install production dependencies
pip install -r requirements.txt

# Run with production server
uvicorn backend:app --host 0.0.0.0 --port 8000
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- PubMed API for providing access to scientific literature
- FastAPI for the excellent web framework
- React and Vite for the modern frontend experience
- Tailwind CSS for the beautiful styling system 