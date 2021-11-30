import React from 'react'
import { Tooltip, XAxis, YAxis, ResponsiveContainer,LineChart,Line, BarChart, Bar,CartesianGrid, Legend } from 'recharts'
export function Graph3(props) {
    const info = [
    {
        subject:"ReactJS",
        project:2,
        
    },
    {
        subject:"Statistics",
        project:6,
    },
    {
        subject:"Calculus",
        project:5,
    },
    {
        subject:"Python",
        project:8,
    },
    {
        subject:"Data Mining",
        project:3,
    },
    
]
    
   
    return (
        <>
 
          <ResponsiveContainer  width="70%" aspect={2}>
              <BarChart width = {50} height = {40} data = {info} barCategoryGap={40} >
              <CartesianGrid strokeDasharray="5 5" />
                  <XAxis interval ={"preserveStartEnd"} dataKey="subject" stroke = "black"/>
                  <YAxis  stroke = "black"/>

                  <Tooltip contentStyle = {{backgroundColor:"white"}} /> 
                  <Legend width={100} wrapperStyle={{ top: 40, right: 20, backgroundColor: '#f5f5f5', border: '1px solid #d5d5d5', borderRadius: 3, lineHeight: '40px' }} />
                  <Bar type="monotone" dataKey = "project" fill = "#FF8042" strokeWidth={1}
                  /> 
                  </BarChart>
          </ResponsiveContainer>
        </>
    )
}