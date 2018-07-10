import {createMuiTheme} from "@material-ui/core/styles/index";

const theme = createMuiTheme({
    palette: {
        primary: {
            light: '#ffab40',
            main: '#ff9100',
            dark: '#ffab40',
            contrastText: '#fff',
        },
        secondary: {
            light: '#ff7961',
            main: '#f44336',
            dark: '#ba000d',
            contrastText: '#000',
        }
    },
});

export default theme;