import React, { useState } from 'react';
import { SearchForm } from './components/SearchForm';
import { ResultsTable } from './components/ResultsTable';
import { ErrorDisplay } from './components/ErrorDisplay';
import { ApiService } from './api';
import { PaperResult } from './types';

function App() {
  const [results, setResults] = useState<PaperResult[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [lastQuery, setLastQuery] = useState('');

  const handleSearch = async (query: string, debug: boolean) => {
    setIsLoading(true);
    setError(null);
    setLastQuery(query);

    try {
      const response = await ApiService.searchPapers({ query, debug });
      
      if (response.error) {
        setError(response.error);
        setResults([]);
      } else {
        setResults(response.results);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unexpected error occurred');
      setResults([]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDownloadCSV = async () => {
    if (!lastQuery) return;

    try {
      const blob = await ApiService.downloadCSV(lastQuery);
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `paperminer_results_${new Date().toISOString().split('T')[0]}.csv`;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
    } catch (err) {
      setError('Failed to download CSV file');
    }
  };

  const handleRetry = () => {
    if (lastQuery) {
      handleSearch(lastQuery, false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-6xl mx-auto">
          <header className="text-center mb-8">
            <h1 className="text-4xl font-bold text-gray-900 mb-2">
              PaperMiner
            </h1>
            <p className="text-lg text-gray-600">
              Discover papers with non-academic authors from pharmaceutical and biotech companies
            </p>
          </header>

          <SearchForm onSearch={handleSearch} isLoading={isLoading} />
          
          {error && (
            <ErrorDisplay error={error} onRetry={handleRetry} />
          )}
          
          {(results.length > 0 || isLoading) && (
            <ResultsTable 
              results={results} 
              onDownloadCSV={handleDownloadCSV}
              isLoading={isLoading}
            />
          )}
        </div>
      </div>
    </div>
  );
}

export default App; 