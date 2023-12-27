import React from 'react'
import PropTypes from 'prop-types'

const Header = () => {
  return (
    <header>
        <h1>Task Tracker</h1>
    </header>
  )
}

Header.defaultProps = {}
Header.propTypes = {
    title: PropTypes.string.isRequired
}

export default Header