import axios from 'axios';
export const api=axios.create({baseURL:import.meta.env.VITE_API_URL??'http://localhost:8000/api'});
export function setToken(token:string){api.defaults.headers.common.Authorization='Bearer '+token}
export const dashboard=()=>api.get('/dashboard/'); export const applications=()=>api.get('/applications/'); export const jobs=()=>api.get('/jobs/');
export const analyzeJob=(job:string,profile:string)=>api.post('/ai/analyze-job/',{job,profile}); export const tailorResume=(job:string,resume:string)=>api.post('/ai/tailor-resume/',{job,resume}); export const coverLetter=(job:string,profile:string)=>api.post('/ai/cover-letter/',{job,profile}); export const interviewPrep=(job:string,application:string)=>api.post('/ai/interview-prep/',{job,application});
