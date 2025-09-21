# Income Analytics Dashboard

A professional interactive web dashboard for analyzing work hours, earnings, and payment tracking with integrated heatmap visualization.

## 🚀 Features

### 📊 Interactive Dashboard
- **Real-time Statistics**: Total hours worked, earnings, payments received, and pending amounts
- **Dynamic Charts**: Multiple chart views including hours overview, earnings analysis, payment comparison, and monthly trends
- **Professional Design**: Modern glassmorphism UI with smooth animations and responsive layout

### 🔥 Integrated Heatmap Table
- **Visual Data Analysis**: Color-coded table cells showing data intensity
- **Multiple Views**: 
  - Hours Heatmap: Visualize work intensity across months
  - Earnings Heatmap: Show income patterns
  - Payments Heatmap: Track payment received patterns
- **Eye-Comfortable Colors**: Soft red-to-green gradient for extended viewing
- **Interactive Tooltips**: Hover for detailed information on each data point

### 📈 Key Insights
- Peak performance month identification
- Payment efficiency tracking
- Average monthly hours calculation
- Earning potential estimates
- Trend analysis and pattern recognition

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Charts**: Chart.js for interactive data visualization
- **Icons**: Font Awesome for professional iconography
- **Data Processing**: Python with pandas and openpyxl for Excel data handling

## 📁 Project Structure

```
Income-Analytics-Dashboard/
├── index.html          # Main dashboard HTML file
├── data.json          # Processed work data in JSON format
├── read_excel.py      # Python script for Excel data processing
├── TOTAL AMOUNT.xlsx  # Source Excel data file
└── README.md          # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3.7+ (for data processing)
- Required Python packages: `pandas`, `openpyxl`

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/curiousboey/Income-Analytics-Dashboard.git
   cd Income-Analytics-Dashboard
   ```

2. **Install Python dependencies**
   ```bash
   pip install pandas openpyxl
   ```

3. **Process Excel data** (if needed)
   ```bash
   python read_excel.py
   ```

4. **Open the dashboard**
   - Simply open `index.html` in your web browser
   - Or serve it locally:
     ```bash
     python -m http.server 8000
     ```
   - Then visit `http://localhost:8000`

## 💾 Data Management

### Excel Data Format
The dashboard expects Excel data with the following columns:
- `MONTH (from 2024)`: Month and year
- `TOTAL HOURS`: Hours worked in that month
- `TOTAL AMOUNT`: Amount earned for that month
- `AMOUNT RECEIVED`: Payment received for that month

### Data Processing
The Python script `read_excel.py` automatically:
- Reads Excel data and cleans unnamed columns
- Converts data to JSON format for web use
- Handles missing values and data formatting

## 🎨 Heatmap Features

### Color Scheme
- **Red**: Low values (needs attention)
- **Yellow**: Average values (moderate performance)
- **Green**: High values (excellent performance)

### Interactive Elements
- **Hover Tooltips**: Detailed information on hover
- **Multiple Views**: Switch between different metric visualizations
- **Smooth Transitions**: Eye-comfortable color animations

## 📊 Dashboard Sections

1. **Summary Statistics Cards**
   - Total hours worked across all months
   - Total earnings and amount received
   - Pending amount calculations

2. **Interactive Charts**
   - Line charts for trend analysis
   - Bar charts for comparative analysis
   - Dynamic data switching

3. **Heatmap Table**
   - Color-coded data visualization
   - Interactive controls for different views
   - Responsive design for all screen sizes

4. **Key Insights Panel**
   - Automated analysis of peak performance
   - Payment efficiency calculations
   - Earning potential estimates

## 🔧 Customization

### Adding New Data
1. Update the Excel file with new monthly data
2. Run `python read_excel.py` to process the data
3. Refresh the dashboard to see updated visualizations

### Styling
- Modify CSS variables in `index.html` for color scheme changes
- Adjust chart configurations in the JavaScript section
- Customize heatmap color ranges as needed

## 📱 Browser Compatibility

- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**curiousboey**
- GitHub: [@curiousboey](https://github.com/curiousboey)

## 🙏 Acknowledgments

- Chart.js for excellent charting capabilities
- Font Awesome for beautiful icons
- Modern CSS techniques for glassmorphism effects

---

*Built with ❤️ for better work analytics and financial tracking*
