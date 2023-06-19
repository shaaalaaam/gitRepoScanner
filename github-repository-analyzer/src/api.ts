import axios from 'axios';

export async function analyzeGitHubUser(url: string): Promise<{ repository: any; complexityScore: number }> {
  try {
    const response = await axios.post('/api/analyze', { url });
    return response.data;
  } catch (error) {
    throw new Error('Failed to analyze GitHub user.');
  }
}
