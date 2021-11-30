import React, { Component } from 'react'

export default class State extends Component {
    constructor(props) {
        super(props)
        
        this.state = {
                 data: ""
        }

    }
    
    show = () =>{ 
        this.setState({
            data: <div style ={{fontFamily:"Poppins",color:"white"}}>
            <br></br>&nbsp;<b>Python</b> is a computer programming language often used to build websites and software, automate tasks, 
            and conduct data analysis. Python is a general purpose language, meaning it can be used to create a 
            variety of different programs and isn't specialized for any specific problems.</div>
     
        })
    }

    show2 = () =>{ 
        this.setState({
            data: <div style ={{fontFamily:"Poppins",color:"white"}}>
                <br></br>&nbsp;<b>Statistics</b> is the study of the collection, analysis, interpretation, 
                presentation, and organization of data. In other words, it is a mathematical 
                discipline to collect, summarize data.
            </div>
     
        })
    }

    show3 = () =>{ 
        this.setState({
            data: <div style ={{fontFamily:"Poppins",color:"white"}}>
                <br></br>&nbsp;<b>Calculus</b> is a branch of mathematics that involves 
                the study of rates of change. Calculus helped to determine how particles, 
                stars, and matter actually move and change in real time.Calculus is used in 
                a multitude of fields that you wouldn't ordinarily think would make use of 
                its concepts. Among them are physics, engineering, economics, statistics, 
                and medicine. Calculus is also used in such disparate areas as space travel, 
                as well as determining how medications interact with the body

            </div>
     
        })
    }
    show4 = () =>{ 
        this.setState({
            data: <div style ={{fontFamily:"Poppins", color:"white"}}>  
                <br></br>&nbsp;<b>ReactJS</b> is a declarative, efficient, and flexible JavaScript library for 
                building reusable UI components. It is an open-source, component-based front 
                end library responsible only for the view layer of the application. It was created 
                by Jordan Walke, who was a software engineer at Facebook. It was initially developed 
                and maintained by Facebook and was later used in its products like WhatsApp and Instagram.
            </div>
        })
    }
    render() {
        return (
            <>
            <h2 style={{fontFamily:"Poppins", fontSize:"20px",color:"white"}}><b>&nbsp;<u>Choose a skill to learn more about:- </u></b></h2>
            
            &nbsp;<button type = "button" onClick = {this.show} style={{fontFamily:"Poppins"}}>Python</button> &nbsp;
            <button type = "button" onClick = {this.show2} style={{fontFamily:"Poppins"}}>Statistics</button> &nbsp;
            <button type = "button" onClick = {this.show3} style={{fontFamily:"Poppins"}}>Calculus</button> &nbsp;
            <button type = "button" onClick = {this.show4} style={{fontFamily:"Poppins"}}>ReactJs</button>
            
            {this.state.data}
            </>
        )
        
    }
}
