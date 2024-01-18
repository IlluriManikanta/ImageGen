import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './index.css';
import App from './App';
import AboutPage from './pages/AboutPage/AboutPage';
import UploadPage from './pages/UploadPage/UploadPage';

// import HomePage from './pages/HomePage/HomePage';
import NotFoundPage from './pages//NotFoundPage/NotFoundPage';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" exact element={<App/>} />
        {/* <Route path="/home" exact element={<HomePage/>} /> */}
        <Route path="/about" element={<AboutPage/>} />
        <Route path="/upload" element={<UploadPage/>} />
        <Route path="*" exact={true} element={<NotFoundPage/>} />
      </Routes>
    </Router>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();