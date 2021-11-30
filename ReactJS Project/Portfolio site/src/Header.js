import React from 'react';
import Home from './Home';
import About from './About';
import Contact from './Contact';
import App from './App.css'
import {Link} from 'react-router-dom'
import {AiTwotoneHome} from 'react-icons/ai';
import {GrContactInfo} from 'react-icons/gr';
import {HiInformationCircle} from "react-icons/hi";

const Header = () => {
    return (
        
        <>
        <div style = {{backgroundColor:"#283593"}} >
        <h1 align = "center" style={{fontFamily:"Patua One", fontSize:"40px", color:"white" }}><u>Manav's Portfolio</u></h1>
        
        </div>
        <ul className = "nav" style={{fontFamily:"Patua One", fontSize:"18px", backgroundColor:"#00C49F"}}>
            <li><a href="/"><AiTwotoneHome/>Home</a></li>
            <li><Link to ="/About"><HiInformationCircle/>About</Link></li>
            <li><Link to ="/Contact"><GrContactInfo size="20px"/>Contact</Link></li>
            <br></br>
            <br></br>
            
        </ul>
        </>
        
    )
}

export default Header