import { defineConfig } from 'vite';
import { VitePWA } from 'vite-plugin-pwa';
import { resolve } from 'path';

export default defineConfig({
  // ... other configuration options

  server: {
    proxy: {
      '/api': 'http://localhost:3001', // Adjust the port number if needed
    },
  },

  plugins: [VitePWA()],

  resolve: {
    alias: {
      '@/': `${resolve(__dirname, 'src')}/`,
    },
  },
});
