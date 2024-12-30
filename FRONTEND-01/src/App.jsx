import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import Hero from "./components/Hero";
import { filterJobs } from "./utils/filters";

import './App.css';
import JobList from "./components/JobList";
import JobDetails from "./components/JobDetails"; // Import JobDetails component
import { jobs } from "./data/jobs";

function App() {
  const [searchQuery, setSearchQuery] = useState('');
  const filteredJobs = filterJobs(jobs, searchQuery);

  return (
    <BrowserRouter>
      <MainLayout>
        <Routes>
          <Route path="/" element={
              <>
                <Hero onSearch={setSearchQuery} />
                <JobList jobs={filteredJobs} />
              </>
            } 
          />
          <Route path="/job-details/:custom_id" element={<JobDetails />} />
          
        </Routes>
      </MainLayout>
    </BrowserRouter>
  );
}

export default App;

