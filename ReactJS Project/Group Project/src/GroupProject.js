import React, {useState, useEffect} from 'react'
import axios from 'axios';

const GroupProject = () => {
  const [chartdata, setChartdata] = useState();
  axios.get("https://raw.githubusercontent.com/manavagarwal1105/My-Files/main/Project%20Dataset.json")
  .then(res =>{
      console.log(res)
  })

  return(
    <div>
        
    </div>
)
}

export default GroupProject