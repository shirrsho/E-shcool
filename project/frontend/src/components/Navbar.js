import { IconButton } from "@material-ui/core";
import { Add, Apps, Menu as MenuIcon } from "@material-ui/icons";
import React from "react";
import "../style/Navbar.css";
function Navbar() {
  const handleClick = (event) => {};

  return (
    <>
      <nav className="navbar">
        <div className="navbar__left">
          <IconButton>
            <MenuIcon />
          </IconButton>

          <span>E-shcool</span>
        </div>
        <div className="navbar__center">
          <span className="route">Materials</span>
          <span className="route">Recordings</span>
          <span className="route">Chatbot</span>
        </div>
        <div className="navbar__right">
          <button>Join Class</button>
          <IconButton
            aria-controls="simple-menu"
            aria-haspopup="true"
            onClick={handleClick}
          >
            <Add />
          </IconButton>
          <IconButton>
            <Apps />
          </IconButton>
          {/* <Menu
            id="simple-menu"
            anchorEl={anchorEl}
            keepMounted
            open={Boolean(anchorEl)}
            onClose={handleClose}
          >
            <MenuItem>Create Class</MenuItem>
            <MenuItem>Join Class</MenuItem>
          </Menu> */}
        </div>
      </nav>
    </>
  );
}
export default Navbar;
