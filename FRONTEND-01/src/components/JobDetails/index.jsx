// import React from 'react'

import { useState, useEffect } from "react";
import { useParams } from "react-router-dom"

const JobDetails = () => {
  const { custom_id } = useParams();
  const [job, setJob] = useState();

  console.log(custom_id)

  console.log(job);
  
  useEffect(() => {
    fetch(`http://localhost:8000/api/job-details/${custom_id}`)
      .then((response) => response.json())
      .then((data) => setJob(data));
  }, [custom_id])


  if (!job) {
    return <p>Loading....</p>
  }
  
  return (
    <div className="container w-full px-4 mx-auto">
      <h1>Job Details</h1>
      <h2>{ job.title }</h2>
      <div dangerouslySetInnerHTML={{ __html: job.full_description }} />
    </div>
  )
}

export default JobDetails