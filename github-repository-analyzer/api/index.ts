import { VercelRequest, VercelResponse } from '@vercel/node';
import analyze from './analyze';

export default function handler(req: VercelRequest, res: VercelResponse) {
  if (req.method === 'POST') {
    return analyze(req, res);
  }

  res.status(405).json({ message: 'Method Not Allowed' });
}
