import React from 'react'
import ReactPaginate from 'react-paginate';
import Grid from '@material-ui/core/Grid';
import {MuiThemeProvider, withStyles} from '@material-ui/core/styles';
import {grey} from '@material-ui/core/colors';

import theme from '../../theme'

const style = {
    pagination:{
        display: 'block',
        paddingLeft: '15px',
        paddingRight: '15px',
        '& ul': {
            paddingLeft: 0,
            listStyle: 'none',
            display: 'flex',
            '& li': {
                ...theme.typography.body1,
                cursor: 'pointer',
                padding: '5px',
                '&:focus': {
                    border: 'none',
                    outline: 'none'
                },
                '& a': {
                    padding: '3px 6px 3px 6px',
                    '&:focus': {
                        border: 'none',
                        outline: 'none'
                    }
                },
                '&.active a': {
                    backgroundColor: theme.palette.primary.main,
                    color: 'white',
                    borderRadius: '50%'
                },
                '&.previous, &.next': {
                    color: theme.palette.primary.main,
                    fontSize: '1rem'
                },
                '&.disabled': {
                    color: grey[400],
                    cursor: 'default'
                }
            }

        }
    }
};

class Pagination extends React.Component {
    constructor(props) {
        super(props);
        this.changePage = this.changePage.bind(this);
    }

    changePage(event){
        this.props.changePage(event.selected);
    }

    render(){
        const {classes} = this.props;

        return (
            <MuiThemeProvider theme={theme}>
                <Grid container justify='center' spacing={16} style={{width: "100%", marginLeft: 0, marginRight: 0}}>
                    <div className={classes.pagination}>
                        <ReactPaginate
                            forcePage={this.props.page}
                            previousLabel={`Anterior <`}
                            nextLabel={`> Próxima`}
                            previousClassName={'previous'}
                            nextClassName={'next'}
                            breakLabel={
                                <a role="button" tabIndex="0" onClick={this.onBreakClick}>
                                    ...
                                </a>
                            }
                            breakClassName={'break-me'}
                            pageCount={Math.ceil(this.props.total/10)}
                            marginPagesDisplayed={2}
                            pageRangeDisplayed={3}
                            onPageChange={this.changePage}
                            subContainerClassName={'pages pagination'}
                            activeClassName={'active'}
                        />
                    </div>
                </Grid>
            </MuiThemeProvider>
        );
    }

}

export default withStyles(style)(Pagination);