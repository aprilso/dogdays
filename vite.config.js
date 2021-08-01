import { defineConfig } from "vite";
import reactRefresh from "@vitejs/plugin-react-refresh";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [reactRefresh()],
  server: {
    proxy: {
      "/api": {
        // only forward routes prefixed with "/api"
        target: "http://localhost:5000", // Flask is running on port 5000
        changeOrigin: true,
        secure: false,
        ws: true,
      },
    },
    fs: {
      // Allow serving files from one level up to the project root
      allow: [".."],
    },
  },
});
