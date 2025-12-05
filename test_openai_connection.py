"""
OpenAI APIの接続テストスクリプト
"""
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込み
load_dotenv()

print("=" * 60)
print("OpenAI API 接続テスト")
print("=" * 60)

# 1. 環境変数の確認
print("\n1. 環境変数の確認:")
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    # セキュリティのため、最初の7文字と最後の4文字のみ表示
    masked_key = f"{api_key[:7]}...{api_key[-4:]}"
    print(f"   ✓ OPENAI_API_KEY: {masked_key}")
    print(f"   キーの長さ: {len(api_key)}文字")
else:
    print("   ✗ OPENAI_API_KEY が設定されていません")
    print("   .envファイルにOPENAI_API_KEYを設定してください")
    exit(1)

# 2. OpenAIライブラリのインポート確認
print("\n2. OpenAIライブラリの確認:")
try:
    from openai import OpenAI
    import openai
    print(f"   ✓ OpenAIライブラリ バージョン: {openai.__version__}")
except ImportError as e:
    print(f"   ✗ OpenAIライブラリのインポートに失敗: {e}")
    exit(1)

# 3. 簡単なAPI呼び出しテスト
print("\n3. OpenAI API 接続テスト:")
try:
    client = OpenAI()
    print("   クライアント作成成功")
    
    # 簡単なチャット補完リクエスト
    print("   API呼び出し中...")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hello"}
        ],
        max_tokens=10
    )
    print(f"   ✓ API接続成功!")
    print(f"   レスポンス: {response.choices[0].message.content}")
    
except Exception as e:
    print(f"   ✗ API接続失敗: {e}")
    print(f"   エラータイプ: {type(e).__name__}")
    exit(1)

# 4. Embeddings APIのテスト
print("\n4. Embeddings API 接続テスト:")
try:
    print("   Embeddings API呼び出し中...")
    from langchain_openai import OpenAIEmbeddings
    embeddings = OpenAIEmbeddings()
    
    # 簡単なテキストの埋め込み
    test_text = "これはテストです"
    result = embeddings.embed_query(test_text)
    print(f"   ✓ Embeddings API接続成功!")
    print(f"   ベクトル次元数: {len(result)}")
    
except Exception as e:
    print(f"   ✗ Embeddings API接続失敗: {e}")
    print(f"   エラータイプ: {type(e).__name__}")
    
    # エラーの詳細を表示
    import traceback
    print("\n   エラー詳細:")
    print(traceback.format_exc())
    exit(1)

print("\n" + "=" * 60)
print("すべてのテストが成功しました!")
print("OpenAI APIは正常に動作しています。")
print("=" * 60)
