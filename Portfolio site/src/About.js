import React from 'react';
import { Graph1 } from './Graph1';
import{GiBookshelf} from "react-icons/gi";
import{GiTrophy} from "react-icons/gi";
import{ImOffice} from "react-icons/im";


const About = () => {
    return (
        <>
        <div>
        <h2 style ={{fontFamily:"Rampart One", fontSize:"30px", color:"#283593"}}>About Me!</h2>
    <div style ={{fontFamily:"Poppins"}}>
        <h3><GiBookshelf size = "23px" color = "#8884d8"/> <u>Academics</u>:-</h3>
        <p>
        Right from my childhood, I was inclined towards technicle subjects like Maths, Chemistry and Physics. Because of my
        interest in these subjects, I was always engaged in academics and focused on my studies. I consider myself as a studious kid who 
        often scored better than his fellow classmates. Even now, I topped my batch and came into the Dean's List at SP Jain. 
        But like every other person, even I had my weakness, LANGUAGES!, I was very weak in languages such as Marathi and Hindi.
        Below is a summary statics which proves my claim of <b>P.C.M</b>("Physics","Chemistry","Math") being by strong subjects.
        </p>
        <Graph1/>   
        
        <h3><GiTrophy size = "20px" color = "#8884d8"/> <u>Achievements</u>:-</h3>
        <p>
        •	The <i>Times of India</i> Certificate of Excellence for qualifying for The City Finale of Times NIE Think and Learn Challenge (Academics)<br></br>
        •	Certificate of Participation for participating in the world’s largest Solar Cooking Festival; officially recognized in <i>Guinness Book of World Record</i> (Cultural)<br></br>
        •	<b>Gold Medal</b>, Intra-gym Hollow Hold Competition (Sports)<br></br>
        •	<b>Silver Medal</b>, Intra-gym Tug of War Competition (Sports)<br></br>
        </p>
        <br></br>
        <h3><ImOffice size = "20px" color = "#8884d8"/> <u>Work Experience</u></h3>
        <p>
        • Writing a research paper at IIT Bombay.<br></br>
        • Working as a data scientist intern at TalentEase.
        </p>
        </div>
        </div>
        </>
    
    )
}

export default About