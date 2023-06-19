import { NextApiRequest, NextApiResponse } from 'next';
import { analyzeGitHubUser } from '../src/api';

export default async function analyzeHandler(req: NextApiRequest, res: NextApiResponse) {
  const { url } = req.body;

  try {
    const { repository, complexityScore } = await analyzeGitHubUser(url);

    res.status(200).json({ repository, complexityScore });
  } catch (error) {
    res.status(500).json({ error: 'Failed to analyze GitHub user.' });
  }
}
