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
            data: 
            <p style ={{color:"white"}}>
            <br></br> 
            <b>&nbsp;•	Hand Cricket Program:</b> A program which plays hand cricket, one of the most common hand games among youngsters of Mumbai. (Individual Project).
            <b>&nbsp;•	Statistical Calculator:</b> A program which calculates statistical parameters such as Mean, Variance, Covariance and Standard Deviation. (Individual Project).
            <b>&nbsp;•	Linear and Multiple Regression:</b> Programs which calculates the simple linear regression equation or the multiple regression equation of the given data.
            <b>&nbsp;•	Object-Oriented Programming:</b> Various object-oriented programs with practical applications such as simple calculator, finding out the outcome of an investment and Tic-Tac-Toe game. (Individual Projects)

            
            </p>
        })
    }

    show2 = () =>{ 
        this.setState({
            data: <div style ={{color:"white"}}>
                <br></br>
                <b>&nbsp;•    Car Sales:</b> Studying and analyzing the sale record of a car company to predict future values.
                <br></br>
            </div>
     
        })
    }

    show4 = () =>{ 
        this.setState({
            data: <div style ={{color:"white"}}>  
                <br></br>
                <b>&nbsp;•    Creating SPA(Single Page Application):</b> Used ReactJS to create a single page student portfolio
                <br></br>
            </div>
        })
    }
    render() {
        return (
            <>
            <h2 style={{fontSize:"20px"}}><b>&nbsp;<u>Overview on some of my projects:- </u></b></h2>
            
            &nbsp;<button type = "button" onClick = {this.show} style={{fontFamily:"Poppins"}}>Python</button> &nbsp;
            <button type = "button" onClick = {this.show2} style={{fontFamily:"Poppins"}}>Statistics</button> &nbsp;
            <button type = "button" onClick = {this.show4} style={{fontFamily:"Poppins"}}>ReactJs</button>
            
            {this.state.data}
            </>
        )
        
    }
}
