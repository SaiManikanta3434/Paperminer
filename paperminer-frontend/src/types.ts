export interface PaperResult {
  PubmedID: string;
  Title: string;
  "Publication Date": string;
  "Non-academic Author(s)": string;
  "Company Affiliation(s)": string;
  "Corresponding Author Email": string;
}

export interface SearchRequest {
  query: string;
  debug?: boolean;
}

export interface SearchResponse {
  results: PaperResult[];
  total: number;
  error?: string;
} 