import React from 'react';
import { Graph2 } from './Graph2';
import State from './State';
import { Graph3 } from './Graph3';
import State2 from'./State2';
const Home = () => {
    
    return (
       <>
       <div>
        <h2 style ={{fontFamily:"Rampart One", fontSize:"30px", color:"#283593"}}>Home Page!</h2>
        <div style ={{fontFamily:"Poppins"}}>
        <p>
            Welcome to my HomePage! My name is Manav Vinay Agarwal. I was born in Mumbai, India. 
            Currently, I am pursuing data science at SP-Jain. To know more about me or to contact me, please click on <b>About</b> and <b>Contact</b> in the Header respectively.

        </p>

        <p>
            After joining SP Jain, I have learnt many skills and honed them. Few of such skills are: 
            Programming, Statistics, Calculus, Data Mining, Leadership Qualities etc. In thhe beginning of my academic year
            I was very weak at technical subjects as I was new to them. Languages such as Python were very difficult for a layman 
            like me. But, after hours of backbreaking and with the help of Sp-Jain's state of the art faculty, I was able to overcome
            my weakness, 
        </p>
        
        <p style={{fontSize:"20px"}}><b><u>Skill Percentage(%)</u></b></p>
        
        <Graph2/>
        
        <div style={{backgroundColor:"#283593"}}>
        <State/>
        </div>
        <br></br>
        
        <p style = {{fontSize:"20px"}}><b><u>Projects</u></b></p>
        <p>
            During my academic term at SP-Jain, I got the opportunity to work on a number of individual as well as 
            group projects. I believe that apart from textual knowledge, it is really very important for students to
            work on projects as it boost their confidence and hone their leadership skills. By working on various projects
            in different subjects, I developed a better understanding and think process. 

        </p>
        <div style = {{backgroundColor:"#00C49F"}}>
        <State2/>
        </div> 
        <br></br>
        <Graph3/>
        </div>
        </div>
        </>
    )
}

export default Home