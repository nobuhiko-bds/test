import java.sql.*;

public class AzureSqlSelectSample {
    public static void main(String[] args) {
        // Azure SQL Database 接続情報
        String url = "jdbc:sqlserver://<your-server>.database.windows.net:1433;database=<your-database>;encrypt=true;trustServerCertificate=false;loginTimeout=30;";
        String user = "<your-username>";
        String password = "<your-password>";

        String query = "SELECT id, name FROM your_table WHERE id = ?";
        int targetId = 1; // 例: id=1の行を取得

        try (Connection conn = DriverManager.getConnection(url, user, password);
             PreparedStatement stmt = conn.prepareStatement(query)) {

            stmt.setInt(1, targetId);

            try (ResultSet rs = stmt.executeQuery()) {
                while (rs.next()) {
                    int id = rs.getInt("id");
                    String name = rs.getString("name");
                    System.out.println("ID: " + id + ", Name: " + name);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
