//For icons, i installed the package : npm install react-icons --save
import React from 'react';
import Photo from './Photo.jpg';
import {AiFillMail} from "react-icons/ai"
import {BiPhoneCall} from "react-icons/bi";

const Contact = () => {
    return (
        <>
        <div>
        <h2 style ={{fontFamily:"Rampart One"}}>Contact Details</h2>
        <img src = {Photo} width="150px"/>
        <div style ={{fontFamily:"Poppins"}}>
        <p> 
            <AiFillMail size = "30px" color = "#8884d8"/>manavagarwal1105@gmail.com <br></br><br></br>
            <BiPhoneCall size = "30px" color = "#8884d8"/> +91 9930391481
            
        </p>
        </div>
        </div>
        </>
    )
}

export default Contact
