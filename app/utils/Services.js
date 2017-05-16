import axios from 'axios'
/*
	Returns a promise in order to set the state of the map component
*/
export const fetchRecords = () => {
	console.log('fetching!!!!!');
  let url = 'http://127.0.0.1:4783/api/records';
  return axios.get(url); 
}