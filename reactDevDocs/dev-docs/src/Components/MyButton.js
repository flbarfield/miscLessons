import { useState } from 'react'

function MyButton() {
    const [count, setCount] = useState(0)
    function handleClick(){
        setCount(count + 1)
    }
    return (
        <button onClick={handleClick}
            style= {{
                'backgroundColor': 'blue',
                'color':'white'
            }}
        >I'm a button! You've clicked me {count} times!</button>
    )
}

export default MyButton