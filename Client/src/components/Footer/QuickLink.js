import React from 'react'

function QuickLink() {
    return (
        <div className="box">
            <h3>quick links</h3>
            <a href="/#"> <i className="fas fa-arrow-right"></i> home </a>
            {/* <a href="/#products"> <i className="fas fa-arrow-right"></i> products </a> */}
            <a href="/#featured"> <i className="fas fa-arrow-right"></i> Our Garden </a>
            <a href="/#review"> <i className="fas fa-arrow-right"></i> Action </a>
            <a href="/#contact"> <i className="fas fa-arrow-right"></i> Contact Us </a>
            <a href="/#blogs"> <i className="fas fa-arrow-right"></i> Blogs </a>
        </div>
    )
}

export default QuickLink
