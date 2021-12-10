//HEADER 

import React from "react"
import App from "./App.css"
//import './syle.css';
import {Link} from "react-router-dom"

const HeaderPage = () => {
    return(
        <div >
             <p
          style={{ color: "Red", backgroundColor: "Black", fontFamily: "Impact", fontWeight: 200, textAlign: 'center',fontSize: 58 }}
        >
          Covid Tracker
        </p>
          
            <ul className="nav">
               <li style={{ color: "Purple", fontFamily: "Impact", fontWeight: 200,textAlign: 'center',fontSize: 30  }}><Link to="/">About Covid</Link></li>
                <li style={{ color: "Purple", fontFamily: "Impact", fontWeight: 200,textAlign: 'center',fontSize: 30 }}><Link to="/GroupCovidTracker">Covid Tracker </Link></li>

            </ul>
        </div>
    )
}

export default HeaderPage



