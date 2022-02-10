<%@ Page Language="VB" %>
  <%@ Register TagPrefix="recaptcha" Namespace="Recaptcha" Assembly="Recaptcha" %>
  <script runat=server%gt;
      Sub btnSubmit_Click(ByVal sender As Object, ByVal e As EventArgs)
          If Page.IsValid Then
              lblResult.Text = "You Got It!"
              lblResult.ForeColor = Drawing.Color.Green
          Else
              lblResult.Text = "Incorrect"
              lblResult.ForeColor = Drawing.Color.Red
          End If
      End Sub
  </script>
  <html>
  <body>
      <form runat="server">
          <asp:Label Visible=false ID="lblResult" runat="server" />
          <recaptcha:RecaptchaControl
              ID="recaptcha"
              runat="server"
              Theme="red"
              PublicKey="your_public_key"
              PrivateKey="your_private_key"
              />

          <asp:Button ID="btnSubmit" runat="server" Text="Submit" OnClick="btnSubmit_Click" />
      </form>
  </body>
  </html>
