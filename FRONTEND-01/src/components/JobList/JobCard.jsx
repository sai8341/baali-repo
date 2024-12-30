// import React from 'react';
import PropTypes from 'prop-types';
import { Building2, MapPin, Clock, ArrowRight, IndianRupee } from 'lucide-react';
import { formatDistanceToNowStrict } from 'date-fns';
import { Link } from "react-router-dom";

const JobCard = ({ job }) => {
  return (
    <div className="p-6 transition-shadow duration-300 bg-white border-l-4 shadow-sm rounded-xl hover:shadow-md border-primary group">
      <div className="flex items-start justify-between">
        <div className="flex-grow">
          <div className="flex items-start justify-between mb-4">
            <h3 className="text-xl font-bold transition-colors text-secondary group-hover:text-primary">
              {job.title}
            </h3>
            <span className="px-3 py-1 text-sm font-medium rounded-full bg-primary/10 text-secondary">
              {job.job_type}
            </span>
          </div>
          <div className="grid grid-cols-2 gap-4 mb-4">
            <div className="flex items-center text-gray-600">
              <Building2 className="w-4 h-4 mr-2 text-primary" />
              <span>{job.company}</span>
            </div>
            <div className="flex items-center text-gray-600">
              <MapPin className="w-4 h-4 mr-2 text-primary" />
              <span>{job.location}</span>
            </div>
            <div className="flex items-center text-gray-600">
              <IndianRupee className="w-4 h-4 mr-2 text-primary" />
              <span>{job.salary || 'N/A'}</span>
            </div>
            <div className="flex items-center text-gray-600">
              <Clock className="w-4 h-4 mr-2 text-primary" />
              <span>{formatDistanceToNowStrict(new Date(job.posted), { addSuffix: true })}</span>
            </div>
          </div>
          <p className="mb-4 text-gray-600">{job.short_description}</p>
          <Link to={`/job-details/${job.custom_id}`} className="flex items-center space-x-2 font-semibold transition-colors text-primary group-hover:text-secondary">
            <span>View Details</span>
            <ArrowRight className="w-4 h-4 transition-transform group-hover:translate-x-1" />
          </Link>
        </div>
      </div>
    </div>
  );
};

JobCard.propTypes = {
  job: PropTypes.shape({
    id: PropTypes.number.isRequired,
    title: PropTypes.string.isRequired,
    company: PropTypes.string.isRequired,
    location: PropTypes.string.isRequired,
    job_type: PropTypes.string.isRequired,
    salary: PropTypes.string,
    posted: PropTypes.string.isRequired, 
    short_description: PropTypes.string.isRequired,
    custom_id: PropTypes.string.isRequired, 
  }).isRequired,
};

export default JobCard;








// JobCard.propTypes = {
//   job: PropTypes.shape({
//     id: PropTypes.number.isRequired,
//     title: PropTypes.string.isRequired,
//     company: PropTypes.string.isRequired,
//     location: PropTypes.string.isRequired,
//     job_type: PropTypes.string.isRequired,
//     salary: PropTypes.string,
//     posted: PropTypes.string.isRequired,
//     short_description: PropTypes.string.isRequired,
//   }).isRequired,
// };

